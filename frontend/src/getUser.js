import api from "./api";
import { useState } from "react";

function getUser() {
    const [user, setUser] = useState([])

    api
        .get("/api/user/")
        .then((res) => res.data)
        .then((data) => {
            setUser(data[0]);
            console.log(data);
        })
        .catch((err) => alert(err));
    return(user)
    }

export default getUser;