odoo.define('attendance.kioskmode', function (require){
    "use strict";
    // var core = require('web.core');
    // require original module JS
    let kiosk = require('hr_attendance.kiosk_mode');
    
    // Extend widget
    kiosk.include({
        events: {
            "click .o_hr_attendance_button_employees": function() {
                this.do_action('attendance-sol.hr_employee_attendance_action_kanban_inherit', {
                    additional_context: {'no_group_by': true},
                });
            },
        }
        },);
})
