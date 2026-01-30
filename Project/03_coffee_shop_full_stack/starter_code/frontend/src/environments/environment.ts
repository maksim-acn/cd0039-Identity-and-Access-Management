/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'udacity-fsnd', // the auth0 domain prefix
    audience: 'dev', // the audience set for the auth0 app
    clientId: 'sFzS7yG4K5L8Q9W0E2R3T4Y5U6I7O8P9', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
