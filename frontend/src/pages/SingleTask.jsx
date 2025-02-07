import { useEffect, useState } from "react";
import { useParams } from "react-router-dom"
import ProtectedRoute from "../components/ProtectedRoute";
import api from "../api";

function SingleTask(){
    const [tasks, setTasks] = useState([])
    const [flag, setFlag] = useState("")
    const { pk } = useParams()
    var error = document.getElementById('error')
    
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
    const errorMessage = (message) => {
        if (message == "Done") {
            error.textContent = "Вы уже сделали это задание!"
            error.style.color = "green"
        }
        else if (message == "Bad") {
            error.textContent = "Пока не правильно, попробуйте ещё раз :("
            error.style.color = "red"
        }
        else if (message == "Good") {
            error.textContent = "Поздравляем, Вы прошли это задание!"
            error.style.color = "green"
        }
        else {
            error.textContent = "Произошла какая-то ошибка ("
            error.style.color = "red"
        }
    }
    const checkTasks = (e) => {
        e.preventDefault();
        api
            .get("api/tasks/check/?task_id=" + pk + "&flag=" + flag)
            .then((res) => res.data)
            .then((data) => {
                errorMessage(data)
                
            })
            .catch((err) => alert(err));
    }
    

    return(
        <ProtectedRoute>
            {tasks.map(task=>
            <div  className="main-root">            
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
                <span id="error"></span><br/>
                <input type="submit" value="Проверить"></input>
                </form>
            </div>)}

        </ProtectedRoute>
        
    )

}

export default SingleTask;