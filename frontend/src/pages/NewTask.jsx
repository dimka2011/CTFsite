import React from "react";
// import "../styles/NewTask.css";
import ProtectedRoute from "../components/ProtectedRoute";

function NewTask() {
    return(
      <ProtectedRoute>
        <div>
        <div className="form-containerr">
        <p className="title">Create new task</p>
        <form>
          <div className="input-groupp">
            <label htmlFor="form-title">Title</label>
            <br />
            <input placeholder="Title" id="form-title"/>
            <br />
            <label htmlFor="form-describtion">Phone</label>
            <br />
            <input placeholder="Describtion" id="form-describtion" />
            <br />
            <label htmlFor="category">Category</label>
            <br />
            <input placeholder="Category" id="category" />
            <br />
            <label htmlFor="flag">Flag</label>
            <br />
            <input placeholder="Flag" id="flag" />
            <br />
            </div>
          <button className="sign">Submit</button>
        </form>
      </div>
    </div>
    </ProtectedRoute>

    )
}

export default NewTask;