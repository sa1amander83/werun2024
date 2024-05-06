import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class NewRunnerForm extends React.Component {
  state = {
    pk: 0,
    user: 0,
    nickname: "",
    runner_team: "",
    runner_age: "",
    runner_category: "",
    zabeg22:false,
    zabeg23:false,

  };

  componentDidMount() {
    if (this.props.runner) {
      const { pk, user, nickname, runner_team, runner_age, runner_category, zabeg22, zabeg23 } = this.props.runner;
      this.setState({ pk, user, nickname, runner_team, runner_age, runner_category, zabeg22, zabeg23 });
    }
  }

  onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  createRunner = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  editRunner = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  };

  defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.runner ? this.editRunner : this.createRunner}>
        <FormGroup>
          <Label for="name">Номер участника</Label>
          <Input
            type="number"
            name="user"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.user)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="nickname">Никнейм</Label>
          <Input
            type="text"
            name="nickname"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.nickname)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="runner_team">Команда</Label>
          <Input
            type="number"
            name="runner_team"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.runner_team)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="runner_age">Возраст</Label>
          <Input
            type="number"
            name="runner_age"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.runner_age)}
          />
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewRunnerForm;