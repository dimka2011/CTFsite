import { useState, useEffect } from "react";
import Task from "../components/Task";
import api from "../api";

function contains(arr, elem) {
    return arr.indexOf(elem) != -1;
 }

 function Tasks(){
    const [user, setUser] = useState([])
    const [userWins, setUserWins] = useState("")
    const [tasks, setTasks] = useState([])
    useEffect(() => {
        getTasks();
        getUser()
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
    const getUser = () => {
        api
            .get("/api/user/")
            .then((res) => res.data)
            .then((data) => {
                setUser(data)
                setUserWins(data[0].win_list)
                console.log("Hello,", data[0].win_list.split(','));
            })
            .catch((err) => alert(err));
    };

    return(
            <div className="main-root">
                <h2>Задачи</h2>
                {tasks.map((task) => (
                    
                    <Task task={task} key={task.id} done = {contains(userWins.split(','), String(task.id))} />
    ))}
    </div>
    )

}

export default Tasks;