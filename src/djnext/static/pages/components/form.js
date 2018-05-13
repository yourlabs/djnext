import Cookie from 'js-cookie'
import React from 'react'
import Button from 'material-ui/Button'
import TextField from 'material-ui/TextField'


export default class extends React.Component {
    constructor(props) {
        super(props)

        this.state = {}
        props.form.fields.map(e => this.state[e.name] = "")

        this.handleChange = this.handleChange.bind(this)
        this.submit = this.submit.bind(this)
    }

    handleChange(name) {
        console.log('handle',name)
        return event => {
            this.setState({ [name]: event.target.value })
        }
    }

    submit(e) {
      console.log('submit', this.state)
      e.preventDefault()
      fetch('', {
        credentials: 'same-origin',
        body: JSON.stringify(this.state),
        method: 'POST',
        headers: {
          'X-CSRFToken': Cookie.get('csrftoken'),
          'Cache-Control': 'no-cache',
          'Accept': 'application/json',
        }
      }).then(res => {
        console.log(res)
        res.text().then(text => {
          console.log(text)
        })
      })
    }

    render() {
        const { fields } = this.props.form

        console.log(fields, this.state, "state")

        const form = fields.map((e, i) => (
            <TextField
                id={ e.name }
                label={ e.label }
                onChange={ this.handleChange(e.name) }
                value={ this.state[e.name] }
                key={ i } />
        ))

        return (
            <div>
                <form ref={ (ref) => this.ref = ref } noValidate autoComplete="off">
                    { form }
                    <Button type="submit" onClick={ this.submit }>Submit</Button>
                </form>
            </div>
        )
    }
}
