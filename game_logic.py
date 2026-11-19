
import time
import asyncio
#from modules.buttondle import buttondle_logic

#Map strings to module names
MODULE_REGISTRY = {
    #"buttondle": buttondle_logic,
}
class BombLogic:
    #This function is used to create an instance of a bomb
    def __init__ (self, on_time_update, on_strike, on_game_over, level_config, duration=300, max_strikes=3):
        #dynamically pass in bomb timer (default 300 seconds/5 minutes)
        self.duration = duration
        #dynamically pass in max strikes before detonation (default 3)
        self.max_strikes = max_strikes
        #current strike incrementor
        self.strikes = 0
        #bomb timer running boolean
        self.is_running = False
        #End_time will be set when the bomb timer is started (self.is_running = true)
        self.end_time = 0
        #on_time_update is used to communicate with the UI to update the clock
        self.on_time_update = on_time_update
        #on_strike is used to communicate with the UI to update the strike counter
        self.on_strike = on_strike
        #on_game_over is used to communicate with the UI when the game is over (strikes reached, timer run out)
        self.on_game_over = on_game_over
        #placeholder for background countdown thread
        self.timer_thread = None


        #---dynamic module instatiation---

        #list of modules installed on the bomb
        self.modules = {}
        #for each pair in 'level_config.items'...
        for mod_id, mod_type in level_config.items():
            #if the module type is in the module_registry...
            if mod_type in MODULE_REGISTRY:
                #create a module on the bomb (with mod_id as an identifier)
                #uses the module_registry to create the associated module
                self.modules[mod_id] = MODULE_REGISTRY[mod_type]()
            else:
                print(f"[WARNING] Module type '{mod_type}' not found in MODULE_REGISTRY.")





    #this function starts the timer of the bomb
    async def run_timer(self):
        self.is_running = True
        self.end_time = time.time() + self.duration
        last_display = ""

        while self.is_running:
            time_left = int(self.end_time - time.time())

            if time_left <= 0:
                self.is_running = False
                self.on_time_update("00:00")
                self.on_game_over("Time ran out.")
                break

            mins, secs = divmod(time_left, 60)
            current_display = f"{mins:02d}:{secs:02d}"

            if current_display != last_display:
                last_display = current_display
                self.on_time_update(current_display)

            # Yield control back to Flet's UI loop cleanly
            await asyncio.sleep(0.1)


    #this logic allows for strike handling (issuing game overs)
    def issue_strike(self, reason="Mistake made!"):
        #if the bomb isnt running, dont issue any strikes
        if not self.is_running:
            return
        #add a strike to the bomb
        self.strikes += 1
        print(f"Strike issued! Total: {self.strikes}/{self.max_strikes} ({reason})")

        #update the UI with new strike count
        self.on_strike(self.strikes, self.max_strikes)

        #if current strikes >= max strikes...
        if self.strikes >= self.max_strikes:
            #end game
            self.is_running = False
            self.on_game_over(f"BOOM! Too many strikes ({reason}).")
            return "exploded"

        return "strike"

    def handle_module_action(self, module_id, action_name, *args):
        """Generic action router that routes UI triggers directly to backend modules."""
        #is game paused?
        if not self.is_running:
            return "game_stopped"
        #does the module name match?
        target_module = self.modules.get(module_id)
        if not target_module:
            return "invalid_module"
        #does the action name match?
        module_method = getattr(target_module, action_name, None)
        if not module_method:
            return "invalid_action"
        #return variable of the module method
        result = module_method(*args)
        #was there a strike?
        if result == "strike":
            return self.issue_strike(f"Mistake in {module_id}")
            
        return result