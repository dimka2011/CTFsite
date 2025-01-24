import { useState, useEffect } from "react";
import Task from "../components/Task";
import api from "../api";

function Tasks(){
    const [tasks, setTasks] = useState([])
    const [user, setUser] = useState([])
    const [userWins, setUserWins] = useState([])
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
                setUserWins(data[0].win_list.split(','))
                console.log(data[0].win_list.split(','));
            })
            .catch((err) => alert(err));
    };

    return(
            <div>
                <h2>Tasks</h2>
                {tasks.map((task) => (
                    <Task task={task} key={task.id} done={String(task.id) in userWins ? (true, console.log(String(task.id)+ "" + userWins)) : false} />
    ))}
    </div>
    )

}

export default Tasks;