<template lang="pug">
.column
  .card
    .card-content
      .content.has-text-centered
        h2 🚨 Last reported price: ${{price}} at {{printDate(date)}} 🚨
</template>

<script>
export default {
  name: 'LastReport',
  props: {
