module.exports = {
  apps: [{
    name: 'Rawww',
    script: './main.js'
  }],
  deploy: {
    production: {
      user: 'ubuntu',
      host: process.env.addy,
      key: process.env.key,
      ref: 'origin/master',
      repo: 'git@github.com:iamjoncannon/Raw.git',
      path: '/home/ubuntu/Raw',
      'post-deploy': 'sudo npm install && sudo pm2 startOrRestart ecosystem.config.js'
    }
  }
}