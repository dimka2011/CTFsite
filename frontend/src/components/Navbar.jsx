import { useState, useEffect } from "react";
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import api from "../api";
import { NavLink } from "react-router-dom";
import "../styles/Navbar.css"


function Navigation(){
    const [user, setUser] = useState([])

    useEffect(() => {
        getUser();
    }, []);
  
    const getUser = () => {
        api
            .get("/api/user/")
            .then((res) => res.data)
            .then((data) => {
                setUser(data);
                console.log(data);
            })
            .catch((err) => setUser(
              [{'id':1,'username':'Login'}]));
    };
    return(
    <Navbar expand="lg" className="bg-body-tertiary" data-bs-theme="dark">
      <Container>
        <Navbar.Brand href="/">CTF</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/leaders">Leaders</Nav.Link>
            {user.map(us => us.username=='Login'?
            <Nav.Link href="/login">Login</Nav.Link> : <NavDropdown title=<b key={us.id}>{us.username}</b> id="basic-nav-dropdown">
              <NavDropdown.Item href="/profile">Profile</NavDropdown.Item>
              <NavDropdown.Item href="/newtask">Create task</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="/logout">
                Logout
              </NavDropdown.Item>
            </NavDropdown>)}

          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
    )
}

export default Navigation;