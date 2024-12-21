import Form from "../components/Form"

function Register() {
    return <div><Form route="/api/user/register/" method="register" /><h4 align="center">Уже есть аккаунт? <a href="/login">Войти</a></h4></div>
}

export default Register
