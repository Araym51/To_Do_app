import React from "react";


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {project: '', users: [], git_link:'' }
    }

    handleUsersChange(event){
        if(!event.target.selectedOptions){
            this.setState({
                'users':[]
            })
            return;
        }

        let  users = []
        for (let i = 0; i < event.target.selectedOptions.length;i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState({
            'users': users
        })
    }

    handleChange(event){
        this.setState(
            {
                [event.target.project]:event.target.value,
                [event.target.git_link]:event.target.value
            }
        )
    }

    handleSubmit(event){
        this.props.createProject(this.state.project,this.state.users, this.state.git_link)
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
                <div className="form-group">
                    <label htmlFor="login">git link</label>
                    <input type="text" className="form-control" name="git_link" value={this.state.git_link}
                           onChange={(event) => this.handleChange(event)}/>
                </div>

                {/*<select name="author" multiple onChange={(event) => this.handleUsersChange(event)}>*/}
                {/*    {this.props.users.map((item) => <option value={item.id}> {item.username} </option>)}*/}

                {/*</select>*/}


                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );

    }

}

export default ProjectForm