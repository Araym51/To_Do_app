// import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from "react";
import axios from "axios";
import {BrowserRouter, HashRouter, Route, Switch} from "react-router-dom";
// my apps:
import UsersList from "./components/Users";
import ToDoList from "./components/ToDo";
import ProjectList from "./components/Projects";
// components:
import {NaviBar} from "./components/Navibar";
import {Footer} from "./components/Footer";



const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users_list': [],
            'todo_list': [],
            'project_list': [],
        }
    }

    componentDidMount() {
        // собираем данные с бэк энда:
        axios.get(get_url('users/')).then(response => {
            const users_list = response.data
            this.setState(
                {
                    'users_list': response.data
                }
            )
        }).catch(error => console.log(error))

        axios.get(get_url('todo/')).then(response => {
            const todo_list = response.data
            this.setState(
                {
                    'todo_list': response.data
                }
            )
        }).catch(error => console.log(error))

        axios.get(get_url('project/')).then(response => {
            const project_list = response.data
            this.setState(
                {
                    'project_list': response.data
                }
            )
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <NaviBar/>
                    <Switch>
                        <Route path='/users/'
                               component={() => <UsersList users_list={this.state.users_list}/>}/>
                        <Route exact path='/todo/'
                               component={() => <ToDoList todo_list={this.state.todo_list}/>}/>
                        <Route exact path='/project/'
                               component={() => <ProjectList project_list={this.state.project_list}/>}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
