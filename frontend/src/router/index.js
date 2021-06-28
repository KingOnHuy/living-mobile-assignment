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
    path: "/store",
    name: "Store",
    component: () => loadView("Store"),
  },
  {
    path: "/category",
    name: "Category",
    component: () => loadView("Category"),
  },
  {
    path: "/menu",
    name: "Menu",
    component: () => loadView("Menu"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => loadView("Login"),
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;
