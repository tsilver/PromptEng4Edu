import streamlit as st
import json
import datetime
from typing import Dict, Any, Optional, Tuple, List, Set
import os

def save_progress_to_indexed_db(data_key: str, data: Dict[str, Any], display_message: bool = True, category: str = "progress") -> None:
    """
    Save progress data to IndexedDB.
    
    Parameters:
    - data_key: Key to store the data under
    - data: Data to store
    - display_message: Whether to display a success message
    - category: Category of data (progress, reflections, completions)
    """
    # Create JavaScript to save to IndexedDB
    js_code = f"""
    async function saveToIndexedDB() {{
        return new Promise((resolve, reject) => {{
            const request = indexedDB.open("PromptEngineeringCourse", 1);
            
            request.onupgradeneeded = function(event) {{
                const db = event.target.result;
                if (!db.objectStoreNames.contains("{category}")) {{
                    db.createObjectStore("{category}");
                }}
            }};
            
            request.onsuccess = function(event) {{
                const db = event.target.result;
                const transaction = db.transaction(["{category}"], "readwrite");
                const store = transaction.objectStore("{category}");
                
                const dataToStore = {json.dumps(data)};
                const saveRequest = store.put(dataToStore, "{data_key}");
                
                saveRequest.onsuccess = function() {{
                    resolve("Data saved successfully");
                }};
                
                saveRequest.onerror = function(e) {{
                    reject("Error saving data: " + e.target.error);
                }};
                
                transaction.oncomplete = function() {{
                    db.close();
                }};
            }};
            
            request.onerror = function(event) {{
                reject("Error opening database: " + event.target.error);
            }};
        }});
    }}
    
    saveToIndexedDB()
        .then(message => {{
            console.log(message);
        }})
        .catch(error => {{
            console.error(error);
        }});
    """
    
    # Execute the JavaScript
    st.components.v1.html(
        f"""
        <script>
        {js_code}
        </script>
        """,
        height=0,
        width=0
    )
    
    # Display success message if requested
    if display_message:
        st.success(f"Your progress has been saved. You can safely exit and return later.")

def load_progress_from_indexed_db(data_keys: list, callback_function: str, category: str = "progress") -> None:
    """
    Load progress data from IndexedDB.
    
    Parameters:
    - data_keys: List of keys to load
    - callback_function: Name of JavaScript function to call with loaded data
    - category: Category of data (progress, reflections, completions)
    """
    # Create JavaScript to load from IndexedDB
    js_code = f"""
    async function loadFromIndexedDB() {{
        return new Promise((resolve, reject) => {{
            const request = indexedDB.open("PromptEngineeringCourse", 1);
            
            request.onupgradeneeded = function(event) {{
                const db = event.target.result;
                if (!db.objectStoreNames.contains("{category}")) {{
                    db.createObjectStore("{category}");
                }}
            }};
            
            request.onsuccess = function(event) {{
                const db = event.target.result;
                const transaction = db.transaction(["{category}"], "readonly");
                const store = transaction.objectStore("{category}");
                
                const dataKeys = {json.dumps(data_keys)};
                const results = {{}};
                
                let remainingKeys = dataKeys.length;
                
                dataKeys.forEach(key => {{
                    const getRequest = store.get(key);
                    
                    getRequest.onsuccess = function(event) {{
                        if (event.target.result) {{
                            results[key] = event.target.result;
                        }}
                        
                        remainingKeys--;
                        if (remainingKeys === 0) {{
                            resolve(results);
                        }}
                    }};
                    
                    getRequest.onerror = function(e) {{
                        console.error("Error retrieving data for key " + key + ": " + e.target.error);
                        remainingKeys--;
                        if (remainingKeys === 0) {{
                            resolve(results);
                        }}
                    }};
                }});
                
                transaction.oncomplete = function() {{
                    db.close();
                }};
            }};
            
            request.onerror = function(event) {{
                reject("Error opening database: " + event.target.error);
            }};
        }});
    }}
    
    loadFromIndexedDB()
        .then(data => {{
            if (typeof {callback_function} === 'function') {{
                {callback_function}(data);
            }} else {{
                console.error("Callback function {callback_function} not found");
            }}
        }})
        .catch(error => {{
            console.error(error);
        }});
    """
    
    # Execute the JavaScript
    st.components.v1.html(
        f"""
        <script>
        {js_code}
        </script>
        """,
        height=0,
        width=0
    )

def get_next_lesson_id(current_lesson: str) -> Optional[str]:
    """
    Calculate the next lesson ID based on the current lesson.
    
    Parameters:
    - current_lesson: Current lesson ID (e.g., "1" for Lesson 1)
    
    Returns:
    - Next lesson ID, or None if there are no more lessons
    """
    # For course introduction, the next lesson is 1
    if current_lesson == "intro":
        return "1"
    
    # For numeric lessons, increment
    try:
        lesson_num = int(current_lesson)
        # Hardcoded maximum lesson number - update as needed
        if lesson_num < 18:  # Assuming there are 18 lessons total
            return str(lesson_num + 1)
        else:
            return None  # No more lessons
    except ValueError:
        # Not a numeric lesson ID
        return None

def get_next_lesson_path(next_lesson_id: str) -> str:
    """
    Get the file path for the next lesson.
    
    Parameters:
    - next_lesson_id: Next lesson ID (e.g., "2" for Lesson 2)
    
    Returns:
    - Path to the next lesson's introduction page
    """
    return f"pages/lesson_{next_lesson_id}_introduction.py"

def save_lesson_completion(lesson_id: str) -> Tuple[bool, Optional[str]]:
    """
    Save lesson completion status.
    
    Parameters:
    - lesson_id: ID of the completed lesson (e.g., "1" for Lesson 1)
    
    Returns:
    - Tuple of (success, next_lesson)
        - success: Whether the operation was successful
        - next_lesson: ID of the next lesson, or None
    """
    # Calculate the next lesson ID
    next_lesson = get_next_lesson_id(lesson_id)
    if not next_lesson:
        return False, None
    
    # Prepare completion data
    completion_data = {
        "completed_at": datetime.datetime.now().isoformat(),
        "next_lesson": next_lesson
    }
    
    # Mark as completed in session state
    st.session_state.setdefault("completed_lessons", {})
    st.session_state["completed_lessons"][lesson_id] = completion_data
    
    # Save to IndexedDB
    save_progress_to_indexed_db(
        f"lesson_{lesson_id}_completion", 
        completion_data, 
        display_message=False,
        category="completions"
    )
    
    return True, next_lesson

def save_reflection_and_navigate(current_lesson: str, reflection_data: dict) -> None:
    """
    Save reflection data, mark the lesson as completed, and navigate to the next lesson.
    
    Parameters:
    - current_lesson: Current lesson ID (e.g., "1" for Lesson 1)
    - reflection_data: Dictionary of reflection data
    """
    # Determine the current page
    if current_lesson == "intro":
        page_name = "course_reflection"
    else:
        page_name = f"lesson_{current_lesson}_reflection"
    
    # Save reflection data
    st.session_state.setdefault("reflections", {})
    st.session_state["reflections"][current_lesson] = reflection_data
    
    # Save reflection to IndexedDB
    save_progress_to_indexed_db(
        f"reflection_{current_lesson}", 
        reflection_data, 
        display_message=False,
        category="reflections"
    )
    
    # Mark lesson as completed
    success, next_lesson = save_lesson_completion(current_lesson)
    
    # Mark the page as completed in session state
    st.session_state.setdefault("completed_pages", set())
    # Use add() for sets instead of append() which is for lists
    st.session_state["completed_pages"].add(page_name)
    
    # Save completed pages to IndexedDB
    save_completed_pages_to_indexeddb()
    
    # Show success message with balloons
    st.balloons()
    st.success(f"🎉 Reflections saved successfully! You've completed {'the course introduction' if current_lesson == 'intro' else f'Lesson {current_lesson}'} and unlocked {'Lesson 1' if current_lesson == 'intro' else f'Lesson {next_lesson}'}.")
    
    # Directly navigate to the next lesson
    if success and next_lesson:
        next_lesson_path = get_next_lesson_path(next_lesson)
        try:
            st.switch_page(next_lesson_path)
        except Exception as e:
            st.error(f"Error navigating to next lesson: {str(e)}")
            st.error(f"Attempted path: {next_lesson_path}")
            st.info("Please navigate manually to the next lesson using the course navigation.")
    else:
        st.error("Error determining the next lesson. Please navigate manually using the course navigation.")

def save_completed_pages_to_indexeddb() -> None:
    """
    Save the set of completed pages to IndexedDB for persistence.
    """
    if "completed_pages" in st.session_state:
        # Convert set to list for JSON serialization
        completed_pages_list = list(st.session_state["completed_pages"])
        
        # Save to IndexedDB
        save_progress_to_indexed_db(
            "completed_pages",
            {"pages": completed_pages_list},
            display_message=False,
            category="completions"
        )

def load_completed_pages_from_indexeddb() -> None:
    """
    Load the set of completed pages from IndexedDB and store in session state.
    """
    # JavaScript callback function to process loaded data
    js_callback = """
    function processCompletedPages(data) {
        if (data && data.completed_pages && data.completed_pages.pages) {
            const completedPages = data.completed_pages.pages;
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: {"completed_pages": completedPages}
            }, "*");
        }
    }
    """
    
    # Execute JavaScript to load data
    st.components.v1.html(
        f"""
        <script>
        {js_callback}
        </script>
        """,
        height=0,
        width=0
    )
    
    # Load from IndexedDB
    load_progress_from_indexed_db(
        ["completed_pages"],
        "processCompletedPages",
        category="completions"
    )
    
    # Handle the loaded data from JavaScript via Streamlit callback
    if "completed_pages" not in st.session_state:
        st.session_state["completed_pages"] = set()
    elif isinstance(st.session_state["completed_pages"], list):
        # Convert from list (from JS) to set
        st.session_state["completed_pages"] = set(st.session_state["completed_pages"])

def clear_indexed_db() -> None:
    """
    Clear all data from IndexedDB for the course.
    """
    # JavaScript to clear IndexedDB
    js_code = """
    async function clearIndexedDB() {
        return new Promise((resolve, reject) => {
            const request = indexedDB.deleteDatabase("PromptEngineeringCourse");
            
            request.onsuccess = function() {
                resolve("Database deleted successfully");
            };
            
            request.onerror = function(event) {
                reject("Error deleting database: " + event.target.error);
            };
            
            request.onblocked = function() {
                // This event is triggered if the database is still open elsewhere
                console.warn("Database deletion blocked");
                resolve("Database deletion blocked, will be deleted when all connections are closed");
            };
        });
    }
    
    clearIndexedDB()
        .then(message => {
            console.log(message);
            // Reload the page to reinitialize everything
            setTimeout(() => window.location.reload(), 500);
        })
        .catch(error => {
            console.error(error);
        });
    """
    
    # Execute the JavaScript
    st.components.v1.html(
        f"""
        <script>
        {js_code}
        </script>
        """,
        height=0,
        width=0
    )
    
    # Clear session state as well
    if "completed_pages" in st.session_state:
        st.session_state["completed_pages"] = set()
    if "completed_lessons" in st.session_state:
        st.session_state["completed_lessons"] = {}
    if "reflections" in st.session_state:
        st.session_state["reflections"] = {}
    
    # Show success message
    st.success("Course progress data has been cleared. The page will reload shortly.")

def get_indexed_db_contents() -> None:
    """
    Retrieve and display the contents of IndexedDB for debugging.
    This function retrieves all data from all stores in IndexedDB
    and sets it in session state for display.
    """
    # JavaScript to get all contents from IndexedDB
    js_code = """
    async function getAllIndexedDBContents() {
        return new Promise((resolve, reject) => {
            const request = indexedDB.open("PromptEngineeringCourse", 1);
            
            request.onupgradeneeded = function(event) {
                const db = event.target.result;
                // Create stores if they don't exist
                if (!db.objectStoreNames.contains("progress")) {
                    db.createObjectStore("progress");
                }
                if (!db.objectStoreNames.contains("reflections")) {
                    db.createObjectStore("reflections");
                }
                if (!db.objectStoreNames.contains("completions")) {
                    db.createObjectStore("completions");
                }
            };
            
            request.onsuccess = function(event) {
                const db = event.target.result;
                const storeNames = Array.from(db.objectStoreNames);
                const allData = {};
                let pendingStores = storeNames.length;
                
                if (pendingStores === 0) {
                    resolve({});
                    return;
                }
                
                storeNames.forEach(storeName => {
                    const storeData = {};
                    const transaction = db.transaction([storeName], "readonly");
                    const store = transaction.objectStore(storeName);
                    const request = store.openCursor();
                    
                    request.onsuccess = function(event) {
                        const cursor = event.target.result;
                        if (cursor) {
                            storeData[cursor.key] = cursor.value;
                            cursor.continue();
                        } else {
                            allData[storeName] = storeData;
                            pendingStores--;
                            if (pendingStores === 0) {
                                resolve(allData);
                                db.close();
                            }
                        }
                    };
                    
                    request.onerror = function(event) {
                        console.error("Error reading store " + storeName + ": " + event.target.error);
                        pendingStores--;
                        if (pendingStores === 0) {
                            resolve(allData);
                            db.close();
                        }
                    };
                });
            };
            
            request.onerror = function(event) {
                reject("Error opening database: " + event.target.error);
            };
        });
    }
    
    getAllIndexedDBContents()
        .then(data => {
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: {"indexed_db_contents": JSON.stringify(data, null, 2)}
            }, "*");
        })
        .catch(error => {
            console.error(error);
            window.parent.postMessage({
                type: "streamlit:setComponentValue",
                value: {"indexed_db_contents": JSON.stringify({error: error}, null, 2)}
            }, "*");
        });
    """
    
    # Execute the JavaScript
    st.components.v1.html(
        f"""
        <script>
        {js_code}
        </script>
        """,
        height=0,
        width=0
    )

def render_teacher_controls_sidebar() -> None:
    """
    Render teacher controls in the sidebar, including:
    - Toggle for teacher content
    - Toggle for debug info
    - Button to clear IndexedDB
    - Toggle for IndexedDB contents
    """
    st.sidebar.title("Teacher Controls")
    st.sidebar.markdown("---")
    
    # Teacher/Student toggle
    st.sidebar.checkbox(
        "Show Teacher Content",
        value=st.session_state.get("show_teacher_content", False),
        key="toggle_teacher_content",
        help="Toggle to show or hide teacher-specific content and notes"
    )
    
    # Debug toggle
    st.sidebar.checkbox(
        "Show Debug Info",
        value=st.session_state.get("show_debug", False),
        key="toggle_debug",
        help="Toggle to show or hide general debug information"
    )
    
    # Clear IndexedDB button
    if st.sidebar.button(
        "🗑️ Clear All Progress Data",
        type="secondary",
        help="This will clear all saved progress and reset the course completely"
    ):
        clear_indexed_db()
    
    # IndexedDB contents toggle
    show_indexeddb = st.sidebar.checkbox(
        "Show IndexedDB Contents",
        value=st.session_state.get("show_indexeddb", False),
        key="toggle_indexeddb",
        help="Toggle to show or hide the contents of the IndexedDB (saved progress data)"
    )
    
    # Fetch and display IndexedDB contents if selected
    if show_indexeddb:
        get_indexed_db_contents()
        
        if "indexed_db_contents" in st.session_state:
            with st.sidebar.expander("IndexedDB Contents", expanded=True):
                try:
                    data = json.loads(st.session_state["indexed_db_contents"])
                    st.write(data)
                except Exception as e:
                    st.error(f"Error parsing IndexedDB contents: {str(e)}")
                    st.code(st.session_state["indexed_db_contents"]) 