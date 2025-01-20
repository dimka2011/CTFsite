
import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css"
import LoadingIndicator from "./LoadingIndicator";

function Form({ route, method }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const name = method === "login" ? "Login" : "Register";

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            const res = await api.post(route, { username, password })
            if (method === "login") {
                localStorage.setItem(ACCESS_TOKEN, res.data.access);
                localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
                navigate("/")
            } else {
                navigate("/login")
            }
        } catch (error) {
            alert(method=="login"?"Неправильное имя или пароль":"Пользователь с таким именем уже существует")
                
        } finally {
            setLoading(false)
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>{name}</h1>
            <input
                className="form-input"
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
            />
            <input
                className="form-input"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
            />
            {loading && <LoadingIndicator />}
            <button className="form-button" type="submit">
                {name}
            </button>
            <h4 align="center">Ещё нет аккаунта? <a href="/register">Зарегестрироваться</a></h4>
        </form>
        // <div class="form-container">
        // <p class="title">{name}</p>
        // <form class="form">
        //     <div class="input-group">
        //         <label for="username">Username</label>
        //         <input type="text" 
        //         name="username" 
        //         id="username" 
        //         value={username}
        //         onChange={(e) => setUsername(e.target.value)}
        //         placeholder="Username"
        //         required />
        //     </div>
        //     <div class="input-group">
        //         <label for="password">Password</label>
        //         <input type="password" 
        //         name="password" 
        //         id="password" 
        //         value={password}
        //         onChange={(e) => setPassword(e.target.value)}
        //         placeholder="Password"
        //         required />
        //         <div class="forgot">
        //             <a rel="noopener noreferrer" href="#">Forgot Password ?</a>
        //         </div>
        //     </div>
        //     <button class="sign">{name}</button>
        // </form>
        // </div>
    );
}

export default Form
