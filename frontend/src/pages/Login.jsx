import Form from "../components/Form"

function Login() {
    return <div><Form route="/api/token/" method="login" align="center"/><h4 align="center">Ещё нет аккаунта? <a href="/register">Зарегестрироваться</a></h4></div>
}

export default Login