import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

function loadView(name) {
  return import(`../views/${name}`);
}

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      loadView('About'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
