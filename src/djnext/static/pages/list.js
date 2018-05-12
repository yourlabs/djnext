import React from 'react'
import Button from 'material-ui/Button'


class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
        }
    }

    render() {
        return (
            <div>
                <Button
                    onClick={ this.props.openDrawer }
                    variant="raised"
                    color="primary">
                    Hello World from list
                </Button>
            </div>
        )
    }
}

export default App
