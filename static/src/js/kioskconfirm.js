odoo.define('attendance.kioskconfirm', function (require) {
    "use strict";

    const core = require('web.core');
    // const ajax = require('web.ajax');
    const QWeb = core.qweb;
    // ajax.loadXML('/attendance/static/src/xml/attendance.xml', QWeb);

    let kioskConfirm = require('hr_attendance.kiosk_confirm');

    kioskConfirm.include({
        init: function (parent, action) {
            this._super.apply(this, arguments);
            this.next_action = 'attendance-sol.hr_attendance_action_kiosk_mode_inherit';
            this.sale_order_line_id = action.sale_order_line_id;
            this.sol_name = action.sol_name;
            this.sol_state = action.sol_state;
            // this.employee_hours_today = field_utils.format.float_time(action.employee_hours_today);
        },
        start: function () {
            var self = this;
            self.$el.html(QWeb.render("HrAttendanceKioskConfirmInherit", {widget: self}));
            self.start_clock();
            return self._super.apply(this, arguments);
        },
        
    });
    
    core.action_registry.add('hr_attendance_kiosk_confirm', kioskConfirm);
})
