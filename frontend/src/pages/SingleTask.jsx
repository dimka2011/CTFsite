import { useEffect, useState } from "react";
import api from "../api";
import { useParams } from "react-router-dom"
import ProtectedRoute from "../components/ProtectedRoute";


function SingleTask(){
    const [tasks, setTasks] = useState([])
    const { pk } = useParams()
    useEffect(() => {
        getTasks();
    }, []);

    const getTasks = () => {
        api
            .get("/api/tasks/"+String(pk) + "/")
            .then((res) => res.data)
            .then((data) => {
                setTasks(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    return(
        <ProtectedRoute>
            {tasks.map(task=>
            <div>            
                <h2>Task</h2>
                <p key={task.id}>{task.title}</p>
            </div>)}

        </ProtectedRoute>
        
    )

}

export default SingleTask;