<template>
  <div class="card recipe-card text-center">
    <img height="150px" :src="product.image_url" class="card-img-top" />
    <div class="card-body">
      <h5 class="card-title">{{ product.item_name }}</h5>

      <h5 class="card-title">စျေးနှုန်း : {{ product.sell_price_per_item }}</h5>
      <p class="card-text">
        <!-- <strong>Ingredients:</strong> {{ recipe.ingredients }} -->
      </p>
      <!-- <div class="action-buttons"> -->
      <nuxt-link :to="`/products/${product.id}/`" class="router-link">
        <p class="gold-text">
          အသေးစိတ်ကြည့်မယ်
        </p>
      </nuxt-link>
      <!-- <nuxt-link :to="`/recipes/${product.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link> -->
      <!-- <button @click="onDelete(product.id)"  class="btn btn-sm btn-danger">Delete</button> -->
      <!-- </div> -->
    </div>
  </div>
</template>
<script>
export default {
  props: ["product", "onDelete"]
};
</script>
<style>
.recipe-card {
  box-shadow: 0 1rem 1.5rem rgba(0, 0, 0, 0.6);
  padding: 5px;
  background-color: rgb(78, 102, 123);
}
.router-link {
  text-decoration: none !important;
  font-size: 12px;
}
.gold-text {
  color: gold;
}
</style>
