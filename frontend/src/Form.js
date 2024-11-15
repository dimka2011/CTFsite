import React, { Component } from "react";
import axios from "axios";

class Form extends Component {
  state = {
    title : "",
    describtion: "",
  };

  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value,
    });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    const { title, describtion } = this.state;

    axios
      .post("http://localhost:8000/api/v1/task", { title, describtion })
      .then((res) => {
        console.log(res.data);
        this.props.addNewItem(res.data);
        this.setState({ title: "", describtion: "" });
      })
      .catch((err) => {
        console.error("Error posting data:", err);
      });
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <div>
          <label>Food:</label>
          <input
            type="text"
            name="title"
            value={this.state.title}
            onChange={this.handleChange}
            required
          />
        </div>
        <div>
          <label>Ingredient:</label>
          <input
            type="text"
            name="describtion"
            value={this.state.decribtion}
            onChange={this.handleChange}
            required
          />
        </div>
        <button type="submit">Add Item</button>
      </form>
    );
  }
}

export default Form;