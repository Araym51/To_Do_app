// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from "react";
import axios from "axios";
import {BrowserRouter, Route, Switch, Link} from "react-router-dom";
//  npm install universal-cookie
import Cookies from "universal-cookie/es6";
// my apps:
import UsersList from "./components/Users";
import ToDoList from "./components/ToDo";
import {ProjectDetail, ProjectList} from "./components/Projects";
import NotFound404 from "./components/NotFound404";

// components:
// import {NaviBar} from "./components/Navibar";
// import {Footer} from "./components/Footer";
import LoginForm from "./components/Auth";
import {Button, Nav, Navbar} from "react-bootstrap";


const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users_list': [],
            'todo_list': [],
            'project_list': [],
            'project_detail': {},
            'token': '',
            'auth' : {username: '', is_login: false},
        }
    }

    getProject(id) {
        // console.log('call')
        // console.log(get_url(`/api/projects/${id}`))
        axios.get(get_url(`project/${id}/`))
            .then(response => {
                this.setState({project_detail: response.data})
            }).catch(error => console.log(error))
        //Разобраться, почему постоянно запрашивает данные:
        // Error: Network Error
        //     at createError (createError.js:17:1)
        //     at XMLHttpRequest.handleError (xhr.js:123:1)
    }

    logout() {
        this.set_token('')
    }

    // собираем данные с бэк энда:
    load_data() {
        const headers = this.get_headers()

        axios.get(get_url('users/'), {headers}).then(response => {
            const users_list = response.data
            this.setState({'users_list': response.data})
        }).catch(error => {
            console.log(error)
            this.setState({'users_list': []})
        })

        axios.get(get_url('todo/', {headers})).then(response => {
            const todo_list = response.data
            this.setState({'todo_list': response.data})
        }).catch(error => {
            console.log(error)
            this.setState({'todo_list': []})
        })

        axios.get(get_url('project/'), {headers}).then(response => {
            const project_list = response.data
            this.setState({'project_list': response.data})
        }).catch(error => {
            console.log(error)
            this.setState({'project_list': []})
        })
    }

    //проверка авторизации по наличию токена:
    is_auth() {
        return !!this.state.token
    }

    // авторизация по токену:
    //  npm install universal-cookie
    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.load_data())
        // localStorage.setItem('token', token)
        // let token_ = localStorage.getItem('token')
        // document.cookie = `token=${token}`
    }

    //собираем токен из cookies
    get_token_from_cookies() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.load_data())
    }

    // собираем токен и имя пользователя:
    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username, password: password
        }).then(response => {
            // console.log(response.data['token'])
            this.set_token(response.data['token'])
        }).catch(error => {
            if (error.response.status === 401) {
                alert('Неверный логин или пароль')
            }else {
                console.log(error)
            }
        })
        // console.log('data= ' + username, password)
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/jsons'
        }
        if (this.is_auth()) {
            headers['Authorization'] = `Token ${this.state.token}`
        }
        return headers
    }

    componentDidMount() {

        this.get_token_from_cookies()
        // this.load_data()
        const username = localStorage.getItem('login')
        if ((username != "") & (username != null)) {
            this.setState({'auth': {username: username, is_login: true}}, () => this.load_data())
        }

    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <NaviBar logout={()=>this.logout()}/>
                    <Switch>
                        <Route path='/login/'
                               component={() => <LoginForm
                                   get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route path='/users/'
                               component={() => <UsersList users_list={this.state.users_list}/>}/>
                        <Route exact path='/todo/'
                               component={() => <ToDoList todo_list={this.state.todo_list}/>}/>
                        <Route exact path='/project/'
                               component={() => <ProjectList project_list={this.state.project_list}/>}/>
                        <Route path="/project/:id/" children={<ProjectDetail getProject={(id) => this.getProject(id)}
                                                                             item={this.state.project_detail}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                {/*<Footer/>*/}
            </div>
        )
    }
}

export default App;
