import App, {Container} from 'next/app'
import Link from 'next/link'
import React from 'react'
import Button from 'material-ui/Button'
import Drawer from 'material-ui/Drawer'
import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List'
import InboxIcon from '@material-ui/icons/Inbox'
import DraftsIcon from '@material-ui/icons/Drafts'

require('es6-promise').polyfill()
require('universal-fetch')

const MenuLink = ({ title, url }) => {
    const styles = {
        a: {
            color: 'inherit',
            textDecoration: 'none',
        },
    }

    return (
        <Link href={ url }>
            <a style={ styles.a }>
                <ListItem button onClick={ () => window.location = url }>
                    <ListItemText
                        primary={ title } />
                </ListItem>
            </a>
        </Link>
    )
}

const MenuLinks = props => {
    const linkList = props.links.map((l, i) => <MenuLink title={ l.title } url={ l.url } key={ i } />)

    const styles = {
        wrapper: {
            width: '200px',
        }
    }

    return (
        <div style={ styles.wrapper }>
            <List component="nav">
                { linkList }
            </List>
        </div>
    )
}


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
                    <MenuLinks links={ this.props.menuLinks } />
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

    if (ctx.query.state) {
      pageProps.serverState = JSON.parse(ctx.query.state)
    } else {
      const res = await fetch('http://localhost:8000/_next/state')
      pageProps.serverState = await res.json()
    }

    return {pageProps}
  }

  state = {
    isOpened: false,
  }

  constructor(props) {
    super(props)

    this.closeDrawer = this.closeDrawer.bind(this)
    this.openDrawer = this.openDrawer.bind(this)
  }

  closeDrawer() {
    this.setState({ isOpened: false })
  }

  openDrawer() {
    this.setState({ isOpened: true })
  }


  render () {
      const {Component, pageProps} = this.props
      const { serverState } = this.props.pageProps

      return (
        <Container>
            <Button
                onClick={ this.openDrawer }
                variant="raised"
                color="primary">
                Open Sidebarssssss
            </Button>
            <Layout
                menuLinks={ serverState.menu }
                openDrawer={ this.openDrawer }
                isOpened={ this.state.isOpened }
                closeDrawer={ this.closeDrawer }>
                <Component
                    openDrawer={ this.openDrawer }
                    { ...pageProps } />
            </Layout>
        </Container>
      )
  }
}
