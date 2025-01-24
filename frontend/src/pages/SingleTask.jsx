import { useEffect, useState } from "react";
import api from "../api";
import { useParams } from "react-router-dom"
import ProtectedRoute from "../components/ProtectedRoute";


function SingleTask(){
    const [tasks, setTasks] = useState([])
    const [flag, setFlag] = useState("")
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
    const checkTasks = (e) => {
        e.preventDefault();
        api
            .get("api/tasks/check/?task_id=" + pk + "&flag=" + flag)
            .then((res) => res.data)
            .then((data) => {
                alert(data);
            })
            .catch((err) => alert(err));
    }

    return(
        <ProtectedRoute>
            {tasks.map(task=>
            <div>            
                <h2>Задание</h2>
                <p key={task.id}>Название: {task.title}</p>
                <p key={task.id}>Описание: {task.content}</p>
                <form onSubmit={checkTasks}>
                <label htmlFor="flag">Введите флаг</label>
                <br />
                <input
                name="flag"
                type="text"
                value={flag}
                onChange={(e) => setFlag(e.target.value)}
                placeholder="Флаг"
                required
                />
                <br />
                <input type="submit" value="Проверить"></input>
                </form>
            </div>)}

        </ProtectedRoute>
        
    )

}

export default SingleTask;