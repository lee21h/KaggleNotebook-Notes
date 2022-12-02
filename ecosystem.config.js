module.exports = {
  apps: [
    {
      name: 'olotc-client',
      cwd: `./client`,
      // exec_mode: 'cluster',
      // instances: 'max', // Or a number of instances
      script: './node_modules/nuxt/bin/nuxt.js',
      args: 'start',
      watch: true,
      restart: true,
    },
    {
      name: "olotc-server",
      cwd: `./server`,
      script: "../../venv/bin/gunicor