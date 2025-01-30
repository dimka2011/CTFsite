
import React from "react";
import "../styles/Task.css"

function Task({ task, done, onDelete }) {
    const formattedDate = new Date(task.created_at).toLocaleDateString("ru-RU")

    return (
        <div className="task-container" >
            <div className="data-container">
                <p className="task-title">{task.title}</p>
                <p className="task-content">{task.content}</p>
                <p className="task-date">{formattedDate}</p>
            </div>
            <div className="link-container">
            {done == true ? (<a href={task.id} className="task-link-done">Сделанно</a>) : (<a href={task.id} className="task-link-try">Выполнить</a>) }
                
            </div>
        </div>
    );
}

export default Task
