
import React from "react";
import "../styles/Task.css"

function Task({ task, done, onDelete }) {
    const formattedDate = new Date(task.created_at).toLocaleDateString("en-US")

    return (
        <div className="task-container">
            <div className="data-container">
                <p className="task-title">{task.title}</p>
                <p className="task-content">{task.content}</p>
                <p className="task-date">{formattedDate}</p>
            </div>
            <div className="link-container">
                {done==true ? (<a href={task.id} className="task-link">Done</a>) : (<a href={task.id} className="task-link">Try</a>)}
                
            </div>
        </div>
    );
}

export default Task
