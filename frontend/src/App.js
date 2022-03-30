import './App.css';
import React from "react";
import {Route, Switch, BrowserRouter,} from "react-router-dom";
import axios from "axios";
//my apps:
import Navibar from "./components/Navibar";
import UsersList from "./components/Users";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import NotFound404 from "./components/NotFound404";
import Home from "./components/Home";
import ProjectDetail from "./components/Project_detail";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'project_detail': {}
        }
    }

    getProject(id) {
        axios.get(`http://127.0.0.1:3000/projects/${id}/`).then(response => {
            this.setState({project_detail: response.data})
        }).catch(error => console.log(error))

    }

    render() {
        return (
            <div>
                <Navibar/>
                <BrowserRouter>
                    <Switch>
                        <Route exact path='/' component={() => <Home/>}/>
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
