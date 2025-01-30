import React from "react";
import { useState, useEffect } from "react";
import api from "../api";


const Leaders = () => {
    const [users, setUsers]  = useState("");
    const [usersWins, setUsersWins] = useState("");
    var wins = []
    useEffect(() => {
        getUsers()
}, []);
    const getUsers = () => {
        api
            .get("/api/users/")
            .then((res) => res.data)
            .then((data) => {
                setUsers(data)
                for (let i=0; i<data.length; i++){
                    wins.push(data[i].win_list.split(',').length)
                }
                setUsersWins(wins)
                console.log(wins)
            })
            .catch((err) => alert(err));
    };
    
    return (
        <div className="main-root">
            <h2>Leaders</h2>

        </div>
    )
}

export default Leaders;