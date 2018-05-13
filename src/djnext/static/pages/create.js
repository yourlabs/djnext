import React from 'react'
import Button from 'material-ui/Button'
import Form from './components/form'

class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
        }
    }

    render() {
        return (
            <div>
                <Form form={ serverState.form } />
            </div>
        )
    }
}

export default App
