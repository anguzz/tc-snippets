<script>
    export let total;
    export let totalArr;
    export let buttons;
    </script>
    
    <style>
      .calculator {
        display: grid;
        grid-template-columns: 24% 24% 24% 24%;
        grid-gap: 5px;
        color: #444;
        border: solid 1px black;
        width: 100%;
        
        padding: 5px;
        background-color: #62a0cc;
        cursor: pointer;
        user-select: none;
      }
    
      #display {
        grid-column: 1 / span 4;
        height: 100px;
        font-size: 1.6rem;
        border: solid 1px black;
        background-color: #62a0cc;
        border-radius: 3px;
        cursor: initial;
        padding: 5px 5px;
        background: linear-gradient(
          135deg,
          #5649e9 0%,
          #4aecc6 37%,
          #b64ed6 58%,
          #6894d3 100%
        );
      }
    
      #display > div {
        text-align: right;
        box-sizing: border-box;
        height: 50%;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
        text-align: right;
        overflow: hidden;
        white-space: nowrap;
      }
    
      #display > div > div {
        float: right;
      }
    
      .top {
        font-size: 0.8em;
        line-height: 200%;
      }
    
      .bottom {
        font-size: 1.2em;
        line-height: 100%;
      }
    
      button {
        height: 40px;
        font-weight: 700;
        font-size: 1.2em;
        cursor: pointer;
      }
    
      #ac {
        grid-column: 1 / span 2;
      }
    
      #clear {
        grid-column: 3 / span 2;
      }
    
      #add {
        height: initial;
        grid-column: 4;
        grid-row: 4 / span 2;
      }
      #equal {
        height: initial;
        grid-column: 4;
        grid-row: 6 / span 2;
      }
      #zero {
        grid-column: 1 / span 2;
      }
    </style>
    
    <div class="calculator">  
        <div id="display"> 
        {#if (total!=='err')}   
        <div>
          <div class="top">{totalArr.join(' ')}</div>
        </div>
        <div>   
          <div class="bottom">{total}</div>
        </div> 
        {:else}
        <div>{total}</div>
        {/if}
      </div>
      {#each buttons as button}
        <button id={button.id} on:click={button.func}>{button.value}</button>
      {/each}
    </div>