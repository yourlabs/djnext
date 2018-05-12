import App, {Container} from 'next/app'
import React from 'react'
import Button from 'material-ui/Button'
import Drawer from 'material-ui/Drawer'
import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List'
import InboxIcon from '@material-ui/icons/Inbox'
import DraftsIcon from '@material-ui/icons/Drafts'

class Layout extends React.Component {
    render() {
        const styles = {
            button: {
                position: 'absolute',
                top: '5rem',
                left: '5rem',
            },
            appWrapper: {
                display: 'flex',
                flex: 1,
                margin: '5vh',
                position: 'relative',
                justifyContent: 'center',
                alignItems: 'center',
            },
        }

        const closeDrawer = () => layoutState.isOpened = false

        return (
            <div>
                <Drawer
                    open={ this.props.isOpened }
                    onClose={ this.props.closeDrawer }>
                    <div
                        tabIndex={0}
                        role="button"
                        onClick={closeDrawer}
                        onKeyDown={closeDrawer}>
                        <List component="nav">
                            <div onClick={ this.props.closeDrawer }>
                                <ListItem button>
                                    <ListItemIcon>
                                        <InboxIcon />
                                    </ListItemIcon>
                                    <ListItemText primary="Inbox" />
                                </ListItem>
                            </div>
                            <ListItem button>
                                <ListItemIcon>
                                    <DraftsIcon />
                                </ListItemIcon>
                                <ListItemText primary="Drafts" />
                            </ListItem>
                        </List>
                    </div>

                    <Button
                        onClick={ this.props.closeDrawer }
                        variant="raised"
                        color="primary">
                        Close Sidebar
                    </Button>
                </Drawer>
                <div style={ styles.button }>
                    <Button
                        onClick={ this.props.openDrawer }
                        variant="raised"
                        color="primary">
                        Open Sidebar
                    </Button>
                </div>
                <div style={ styles.appWrapper }>
                    { this.props.children }
                </div>
            </div>
        )
    }
}

export default class MyApp extends App {
  static async getInitialProps ({ Component, router, ctx }) {
    let pageProps = {}

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx)
    }

    return {pageProps}
  }

  render () {
    const {Component, pageProps} = this.props
    return <Container>
      <Button variant="raised" color="primary">
        Hello World from layout
      </Button>
      <Component {...pageProps} />
    </Container>
  }
}
