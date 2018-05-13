import React from 'react'
import TextField from 'material-ui/TextField'


export default class extends React.Component {
    constructor(props) {
        super(props)

        const state = {}
        this.state = props.form.fields.map(e => state[e.name] = "")

        this.handleChange = this.handleChange.bind(this)
    }

    handleChange(name) {
        return event => this.setState({ [name]: event.target.value })
    }

    render() {
        const { fields } = this.props.form

        console.log(fields, this.state, "state")

        const form = fields.map((e, i) => (
            <TextField
                id={ e.name }
                label={ e.label }
                onChange={ this.handleChange }
                value={ this.state[e.name] }
                key={ i } />
        ))

        return (
            <div>
                <form noValidate autoComplete="off">
                    { form }
                </form>
            </div>
        )
    }
}
