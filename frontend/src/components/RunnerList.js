import React, { Component } from "react";
import { Table } from "reactstrap";
import NewStudentModal from "./NewRunnerForm";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

class RunnerList extends Component {
  render() {
    const runners = this.props.runners;
    return (
      <Table dark>
        <thead>
          <tr>
            <th>id</th>
            <th >номер участника</th>
            <th >никнейм</th>
            <th >команда</th>
            <th >возраст</th>
            <th >категория</th>
          </tr>
        </thead>
        <tbody>
          {!runners || runners.length <= 0 ? (
            <tr>
              <td colSpan="6" align="center">
                <b>Ops, no one here yet</b>
              </td>
            </tr>
          ) : (
            runners.map(runner => (
              <tr key={runner.pk}>
                <td >{runner.user}</td>
                <td >{runner.nickname}</td>
                <td >{runner.runner_age}</td>
                <td >{runner.runner_category}</td>
                <td >{runner.runner_team}</td>
                <td align="center">
                  <NewStudentModal
                    create={false}
                    runner={runner}
                    resetState={this.props.resetState}
                  />
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    pk={runner.pk}
                    resetState={this.props.resetState}
                  />
                </td>
              </tr>
            ))
          )}
        </tbody>
      </Table>
    );
  }
}

export default RunnerList;