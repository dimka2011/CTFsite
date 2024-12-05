import { useState, useEffect } from "react";
import api from "../api";
import Task from "../components/Task"
import "../styles/Home.css"

function Home() {
    const [tasks, setTasks] = useState([]);
    const [categories, setCategories] = useState([]);
    const [describtion, setDescribtion] = useState("");
    const [title, setTitle] = useState("");
    const [flag, setFlag] = useState("");
    const [category, setCategory] = useState("");

    useEffect(() => {
        getTasks();
        getCategories();
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
    const getCategories = () => {
        api
            .get("/api/category/")
            .then((res) => res.data)
            .then((data) => {
                setCategories(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };


    const deleteTask = (id) => {
        api
            .delete(`/api/tasks/delete/${id}/`)
            .then((res) => {
                if (res.status === 204) alert("Task deleted!");
                else alert("Failed to delete Task.");
                getTasks();
            })
            .catch((error) => alert(error));
    };
    const createTask = (e) => {
        e.preventDefault();
        api
            .post("/api/tasks/", {"describtion": "describtion","title": "title","flag": "flag","category": 1})
            .then((res) => {
                if (res.status === 201) alert("Task created!");
                else alert("Failed to make task.");
                getTasks();
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                <h2>Tasks</h2>
                {tasks.map((task) => (
                    <Task task={task} onDelete={deleteTask} key={task.id} />
                ))}
            </div>
            <h2>Create a task</h2>
            <form onSubmit={createTask}>
                <label htmlFor="title">Title:</label>
                <br />
                <input
                    type="text"
                    id="title"
                    name="title"
                    required
                    onChange={(e) => setTitle(e.target.value)}
                    value={title}
                />
                <label htmlFor="describtion">Описание:</label>
                <br />
                <textarea
                    id="describtion"
                    name="describtion"
                    required
                    value={describtion}
                    onChange={(e) => setDescribtion(e.target.value)}
                ></textarea>
                <label htmlFor="flag">Флаг:</label>
                <br />
                <input
                    type="text"
                    id="flag"
                    name="flag"
                    required
                    onChange={(e) => setFlag(e.target.value)}
                    value={flag}
                />
                <label htmlFor="category">Флаг:</label>
                <br />
                <select
                    id="category"
                    name="category"
                    required
                    default="Easy"
                    onChange={(e) => setCategory(e.target.value)}
                    // value={category}
                >
                    {categories.map((cat) => (
                    <option value={cat.id} key={cat.id}>{cat.title}</option>
                ))}
                </select>/
                <br />
                <input type="submit" value="Submit"></input>
            </form>
        </div>
    );
}

export default Home;