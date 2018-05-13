import React from 'react'
import Button from 'material-ui/Button'


class App extends React.Component {
    constructor(props) {
        super(props)

        this.state = {
        }
    }

    render() {
        const { results } = this.props.serverState.object_list
        const list = results.map((e, i) => <div key={ i }>{ e.name }</div>)

        return (
            <div>
                <Button
                    onClick={ this.props.openDrawer }
                    variant="raised"
                    color="primary">
                    Hello World from list
                </Button>
                { list }
            </div>
        )
    }
}

export default App
