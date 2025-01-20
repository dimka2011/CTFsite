import react from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Tasks from "./pages/Tasks"
import NotFound from "./pages/NotFound"
import ProtectedRoute from "./components/ProtectedRoute"
import UserProfile from "./pages/Profile"
import "./index.css"
import SingleTask from "./pages/SingleTask"
import { useState, useEffect } from "react"
import NewTask from "./pages/NewTask"
import Navigation from './components/Navbar.jsx';


function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <div>
    <BrowserRouter>
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Navigation />
              <Tasks />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="/profile" element={<div><Navigation /><UserProfile /></div>} />
        <Route path="/:pk" element={<div><Navigation /><SingleTask /></div>} />
        <Route path="/newtask" element={<div><Navigation /><NewTask /></div>}/>

        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
    </div>
  )
}

export default App