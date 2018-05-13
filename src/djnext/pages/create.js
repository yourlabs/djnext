import React from 'react'
import Button from 'material-ui/Button'
import Form from './components/form'

export default class extends React.Component {
    constructor(props) {
        super(props)

        this.state = {}
    }

    render() {
        return (
            <div>
                <Form form={ this.props.serverState.form } />
            </div>
        )
    }
}
