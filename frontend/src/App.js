import './App.css';
import React from "react";
import {Route, Switch, BrowserRouter,} from "react-router-dom";
import axios from "axios";
import Cookies from "universal-cookie/es6";
//my apps:
import Navibar from "./components/Navibar";
import UsersList from "./components/Users";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import NotFound404 from "./components/NotFound404";
import Home from "./components/Home";
import ProjectDetail from "./components/Project_detail";
import LoginForm from "./components/Login";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project_detail': {},
            'token': '',
        }
    }

    is_aut() {
        return !!this.state.token
    }

    //уствновка токена
    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, () => this.get_headers())
        console.log(this.state.token)
    }

    // получение токена из куков
    get_token_from_cookies() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, () => this.get_headers())
    }

    //получение токена
    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/',
            {username: username, password: password}
        ).then(response => {
            this.set_token(response.data['token'])
            localStorage.setItem('login', username)
        }).catch(error => console.log(error))
    }

    get_headers() {
        console.log('test')
        let headers = {
            'Content-Type': 'application/json'
        }
        console.log(this.is_aut())
        if (this.is_aut()) {
            console.log(`Token ${this.state.token}`)
            headers['Authorization'] = `Token ${this.state.token}`
        }
        return headers
    }

    // 8000?
    getProject(id) {
        axios.get(`http://127.0.0.1:3000/projects/${id}/`).then(response => {
            this.setState({project_detail: response.data})
        }).catch(error => console.log(error))

    }

    logout() {
        localStorage.setItem('login', '')
        this.set_token('')
        console.log('LOGOUT!')
    }

    componentDidMount() {
        this.get_token_from_cookies()

    }

    render() {
        return (
            <div>
                {/*todo: победить logout!*/}
                <Navibar logout={() => this.logout()}/>
                <BrowserRouter>
                    <Switch>
                        <Route exact path='/' component={() => <Home/>}/>
                        <Route path='/login/'
                               component={() => <LoginForm
                                   get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route exact path='/users' component={() => <UsersList/>}/>
                        <Route exact path='/projects' component={() => <ProjectList/>}/>
                        <Route exact path='/todo' component={() => <ToDoList/>}/>
                        <Route path="/projects/:id/" children={<ProjectDetail getProject={(id) => this.getProject(id)}
                                                                              item={this.state.project_detail}/>}/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
            </div>
        );
    }
}

export default App;
