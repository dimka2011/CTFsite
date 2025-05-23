import React from "react";
import { useState } from "react";
import api from "../api";
// import "../styles/NewTask.css";
import ProtectedRoute from "../components/ProtectedRoute";

function NewTask() {
    const [title, setTitle] = useState("")
    const [content, setContent] = useState("")
    const [category, setCategory] = useState("")
    const [flag, setFlag] = useState("")
    const createTask = (e) => {
      e.preventDefault();
      api
            .post("/api/tasks/create/", {title, content, category, flag})
            .then((res) => res.data)
            .then((data) => {
              alert("Success")
            })
            .catch((err) => alert(err));

    }
    return(
      <ProtectedRoute>
        <div  className="main-root">
        <div className="form-containerr">
        <p className="title">Create new task</p>
        <form onSubmit={createTask}>
          <div className="input-groupp">
            <label htmlFor="form-title">Title</label>
            <br />
            <input placeholder="Title" 
            id="form-title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            />
            <br />
            <label htmlFor="form-describption">Describtion</label>
            <br />
            <input placeholder="Describtion" 
            id="form-describption" 
            value={content}
            onChange={(e) => setContent(e.target.value)}
            required
            />
            <br />
            <label htmlFor="category">Category</label>
            <br />
            <input placeholder="Category" 
            id="category" 
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
            />
            <br />
            <label htmlFor="flag">Flag</label>
            <br />
            <input placeholder="Flag" 
            id="flag" 
            value={flag}
            onChange={(e) => setFlag(e.target.value)}
            required
            />
            <br />
            </div>
            <input type="submit" value="Submit" />
        </form>
      </div>
    </div>
    </ProtectedRoute>

    )
}

export default NewTask;