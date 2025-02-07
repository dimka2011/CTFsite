import { useState, useEffect, useMemo } from "react";
import api from "../api";
import ProtectedRoute from "../components/ProtectedRoute";

function UserProfile(){
    const [user, setUser] = useState([])
    const [bio, setBio] = useState("")
    const [birth_date, setBirth_date] = useState("")
    const [first_name, setFirst_name] = useState("")
    const [last_name, setLast_name] = useState("")
    const [location, setLocation] = useState("")
    const [email, setEmail] = useState("")
    // const options = useMemo(() => countryList().getData(), [])
    useEffect(() => {
        getUser();
    }, []);
    const updateUser = (e) => {
        e.preventDefault();
        api
            .put("api/user/update/", { bio, birth_date, first_name, last_name, location, email })
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
                setBio(data.bio)
                setBirth_date(data.birth_date)
                setEmail(data.email)
                setFirst_name(data.first_name)
                setLast_name(data.last_name)
                setLocation(data.location)
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    return(
        <ProtectedRoute>
            <div className="main-root">
                <h2>Профиль</h2>
                {user.map(us => (
                <div>
                <p key={us.id}>Username: {us.username}, wins: {us.win_list.split(',').length - 1}</p>
                 
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
                <label htmlFor="birth_date">Дата рождения</label>
                <br />
                <input
                    type="date"
                    id="birth_date"
                    name="birth_date"
                    defaultValue={us.birth_date}
                    onChange={(e) => setBirth_date(e.target.value)}
                />
                <br />
                <label htmlFor="email">Почта</label>
                <br />
                <input
                    type="email"
                    id="email"
                    name="email"
                    defaultValue={us.email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <br />
                <label htmlFor="first_name">Имя</label>
                <br />
                <input
                    type="text"
                    id="first_name"
                    name="first_name"
                    defaultValue={us.first_name}
                    onChange={(e) => setFirst_name(e.target.value)}
                />
                <br />
                <label htmlFor="last_name">Фамилия</label>
                <br />
                <input
                    type="text"
                    id="last_name"
                    name="last_name"
                    defaultValue={us.last_name}
                    onChange={(e) => setLast_name(e.target.value)}
                />
                <br />
                {/* <label htmlFor="last_name">Город</label>
                <br />
                <Select
                    id="location"
                    name="location"
                    options={options}
                    value={location} 
                    onChange={changeLocation} />
                <br />
                <CountryDropdown
                value={location}
                onChange={(value) => changeLocation(value)} /> */}
                <input type="submit" value="Submit" />
                </form>
                </div>
            ))}</div>
    </ProtectedRoute>
    )

    }

export default UserProfile;