import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import RunnerList from "./RunnerList";
import NewRunnerModal from "./NewRunner";

import axios from "axios";

import { API_URL } from "../constants";


class Home extends Component {
  state = {
    runners: []
  };

  componentDidMount() {
    this.resetState();
  }

  getRunners = () => {
    axios.get(API_URL).then(res => this.setState({ runners: res.data }));
  };

  resetState = () => {
    this.getRunners();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            <RunnerList
              runners={this.state.runners}
              resetState={this.resetState}
            />
          </Col>
        </Row>
        <Row>
          <Col>
            <NewRunnerModal create={true} resetState={this.resetState} />
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;