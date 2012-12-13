from boto.ec2 import connect_to_region
import argparse




def make_hosts_file(opts):

    ec2  = connect_to_region(opts.region)
    instances = []
    reservations = ec2.get_all_instances()
    for r in reservations:
        for i in r.instances:
            instances.append(i)

    for i in instances:
        if i.public_dns_name:
            for name in [i.public_dns_name,i.ip_address] :
                print "Host %s" % name
                print "    IdentityFile %s/%s.pem"  % (opts.id_file_dir,i.key_name)
                print "    User %s" % opts.user
                for extra in opts.extra_args:
                    print "    %s" % extra

def main():

    parser = argparse.ArgumentParser("make an ssh hosts file for your all your pretty little ec2  instances. you can append the output to your .ssh config file if you want, in  ~/.ssh/config, but don't take my word for it!")
    parser.add_argument("--id-file-dir",default="~/.ssh",required=False)
    parser.add_argument("--user",default="ubuntu",required=False)
    parser.add_argument("--region",default="eu-west-1",required=False)
    parser.add_argument("--extra-args",type=str,action='append',default=[],required=False)
    make_hosts_file(parser.parse_args())

if __name__ == "__main__" : main()
    
