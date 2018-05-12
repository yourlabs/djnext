import App, {Container} from 'next/app'
import React from 'react'
import Button from 'material-ui/Button'

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
