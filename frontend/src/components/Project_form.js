import React from "react";
import {Form, FormSelect} from "react-bootstrap";


class ProjectForm extends React.Component {
    // handleUsersChange(event) {
    //     if (!event.target.selectedOptions) {
    //         this.setState({
    //             'users': []
    //         })
    //         return;
    //     }
    //
    //     let users_list = []
    //     for (let i = 0; i < event.target.selectedOptions.length; i++) {
    //         users_list.push(event.target.selectedOptions.item(i).value)
    //     }
    //     this.setState({
    //         'users_list': users_list
    //     })
    // }

    //             {/*<select name="users" multiple onChange={(event) => this.handleUsersChange(event)}>*/}
    //             {/*    {this.props.users.map((item) => <option value={item.id}> {item.username} </option>)}*/}
    //
    //             {/*</select>*/}
    //
    //             <p></p>
    //             <input type="submit" className="btn btn-primary" value="Save"/>

    constructor(props) {
        super(props);
        this.state = {project: "", git_link: ""}
    }

        handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        )
        console.log(event.target.name, event.target.value)
    }

    handleSubmit(event) {
        this.props.createProject(this.state.project, this.state.git_link)
        console.log(this.state.project)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                 <div className="form-group">
                     <label for="login">project</label>
                     <input type="text" className="form-control" name="project" value={this.state.project}
                            onChange={(event) => this.handleChange(event)}/>
                 </div>
                <p></p>
                <div className="form-group">
                    <label htmlFor="login">project</label>
                    <input type="text" className="form-control" name="git_link" value={this.state.git_link}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <p></p>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>


        )
    }
}

export default ProjectForm