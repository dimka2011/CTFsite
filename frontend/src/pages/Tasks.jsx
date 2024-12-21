import { useState, useEffect } from "react";
import Task from "../components/Task";
import api from "../api";

function Tasks(){
    const [tasks, setTasks] = useState([])

    useEffect(() => {
        getTasks();
    }, []);

    const getTasks = () => {
        api
            .get("/api/tasks/")
            .then((res) => res.data)
            .then((data) => {
                setTasks(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    return(
            <div>
                <h2>Tasks</h2>
                {tasks.map((task) => (
                    <Task task={task} key={task.id} />
    ))}
    </div>
    )

}

export default Tasks;