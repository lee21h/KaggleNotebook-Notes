
<template lang="pug">
section.section
  .column
    .card
      .card-content
        .container
          .content.has-text-centered
            .title Submit new OTC trade
            b-field(grouped, group-multiline)
              b-input(v-model='amount', type='number', min='0', step="any", placeholder='GAS amount sold')
              b-input(v-model='price', type='number', min='0', step="any", placeholder='Price per coin ($)')
              b-datetimepicker(
                v-model='selectedDatetime',
                placeholder='Click to select datetime',
                icon='calendar-today',
                :icon-right="selectedDatetime ? 'close-circle' : ''",
                icon-right-clickable,
                @icon-right-click='clearDateTime',
                :locale='locale',
                :first-day-of-week='firstDayOfWeek',
                :datepicker='{ showWeekNumber }',
                :timepicker='{ enableSeconds, hourFormat }',
                horizontal-time-picker)

              b-button(type='is-primary', outlined, @click="submitTrade") Submit
</template>
<script>
export default {
  name: 'TradeReport',
  data() {
    return {
      amount: null,
      price: null,
      selectedDatetime: null,
      showWeekNumber: false,