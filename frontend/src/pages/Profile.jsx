import { useState, useEffect } from "react";
import api from "../api";
import ProtectedRoute from "../components/ProtectedRoute";

function UserProfile(){
    const [user, setUser] = useState([])
    const [bio, setBio] = useState("")
    const [birthDate, setBirthDate] = useState("")
    useEffect(() => {
        getUser();
    }, []);
    const updateUser = (e) => {
        e.preventDefault();
        api
            .put("api/user/update/", { bio, birthDate })
            .then((res) => {
                if (res.status === 200) alert("Successfully updated");
                else alert("Failed to update.");
            })
            .catch((err) => alert(err));
    };
    const getUser = () => {
        api
            .get("/api/user/")
            .then((res) => res.data)
            .then((data) => {
                setUser(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    return(
        <ProtectedRoute>
            <div>
                <h2>User</h2>
                {user.map(us => (
                <div>
                <p key={us.id}>{us.username}</p>
                 
                <form onSubmit={updateUser}>
                <label htmlFor="bio">Биография:</label>
                <br />
                <input
                    type="text"
                    id="bio"
                    name="bio"
                    defaultValue={us.bio}
                    onChange={(e) => setBio(e.target.value)}
                />
                <br />
                <label htmlFor="birthDate">Дата рождения</label>
                <br />
                <input
                    type="date"
                    id="birth_date"
                    name="birth_date"
                    defaultValue={us.birth_date}
                    onChange={(e) => setBirthDate(e.target.value)}
                />
                <br />
                <input type="submit" value="Submit"></input>
                </form>
                </div>
            ))}</div>
    </ProtectedRoute>
    )

    }

export default UserProfile;